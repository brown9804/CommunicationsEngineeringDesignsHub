// C
// Implementing the Huffman Coding algorithm, Open source.
// Brandon Esquivel
// U.C.R
// September, 2020
// implement the minimal prefix coding algorithm by David Huffman


// Includes
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

// DEFINES
#define MAX_BUFFER_SIZE 256
#define INVALID_BR -1
#define INVALID_BW -1

// Global variables
int syms = 256;
int num_active = 0;
int *frequency = NULL;
unsigned int original_size = 0;

/* Define Structure stages to control de nodes logic. For each node in the binary coding tree, we shall maintain
two values. An index to identify the node, and a weight
assigned to that node. The weight of a leaf node equals the
corresponding alphabet frequency; the weight of an internal
node equals the sum of the weights of its children. To
differentiate between leaf nodes and internal nodes, we use
the sign of the index*/
typedef struct {
    int index;
    unsigned int weight;
} stages;
stages *nodes = NULL;
int num_nodes = 0;
int *leaf_index = NULL;
int *parent_index = NULL;
int free_index = 1;
int *stack;
int stack_top;
unsigned char buffer[MAX_BUFFER_SIZE];
int bits_in_buffer = 0;
int current_bit = 0;
int eof_input = 0;

// methods, fuctions

int read_header(FILE *f);
int write_header(FILE *f);
int read_bit(FILE *f);
int write_bit(FILE *f, int bit);
int flush_buffer(FILE *f);
void decode_bit_stream(FILE *fin, FILE *fout);
int decode(const char* ifile, const char *ofile);
void encode_alphabet(FILE *fout, int character);
int encode(const char* ifile, const char *ofile);
void build_tree();
void add_leaves();
int add_node(int index, int weight);
void finalise();
void init();


/*The function determine_frequency() calculates the frequency
for each of the alphabets by parsing the input data stream
completely. It also counts the number of bytes in the stream*/
void determine_frequency(FILE *f) {
    int c;
    while ((c = fgetc(f)) != EOF) {
        ++frequency[c];
        ++original_size;
    }
    for (c = 0; c < syms; ++c)
        if (frequency[c] > 0)
            ++num_active;
}

/*initialise the program by allocating space for maintaining the alphabet frequencies, and the leaf-to-node
index lookup table, since they are already known in advance irrespective
of the input data stream. We ensure that leaf_index is adjusted
to match indexing that begins at 1.*/
void init() {
    frequency = (int *)
        calloc(2 * syms, sizeof(int));
    leaf_index = frequency + syms - 1;
}

/*Allocate space for the coding tree nodes and parent index
look-up table. Due to the manner in which the coding tree is
built, we can assert that every internal node has two children.
This makes the coding tree a full binary tree*/

void allocate_tree() {
    nodes = (stages *)
        calloc(2 * num_active, sizeof(stages));
    parent_index = (int *)
        calloc(num_active, sizeof(int));
}

/*Just free memory*/
void finalise() {
    free(parent_index);
    free(frequency);
    free(nodes);
}

/* Function to add a new node of the tree*/
int add_node(int index, int weight) {
    int i = num_nodes++;
    while (i > 0 && nodes[i].weight > weight) {
        memcpy(&nodes[i + 1], &nodes[i], sizeof(stages));
        if (nodes[i].index < 0)
            ++leaf_index[-nodes[i].index];
        else
            ++parent_index[nodes[i].index];
        --i;
    }

    ++i;
    nodes[i].index = index;
    nodes[i].weight = weight;
    if (index < 0)
        leaf_index[-index] = i;
    else
        parent_index[index] = i;

    return i;
}
/*Before we build the tree, we first insert all of the leaves for
which we already know the weights.*/
void add_leaves() {
    int i, freq;
    for (i = 0; i < syms; ++i) {
        freq = frequency[i];
        if (freq > 0)
            add_node(-(i + 1), freq);
    }
}

/**When there are node pairs that could be combined, we create
a new node with the pair as children, and add the new node
to the tree. Notice here that because we always combined two
consecutive free nodes, the parents for both these nodes can
be maintain in the shared parent_index table using a single
value. We store the same parent index in the node, which does
not have a special meaning for internal nodes, so that node
indices can be updated as the tree structure changes*/
void build_tree() {
    int a, b, index;
    while (free_index < num_nodes) {
        a = free_index++;
        b = free_index++;
        index = add_node(b/2,
            nodes[a].weight + nodes[b].weight);
        parent_index[b/2] = index;
    }
}

/*read the input bytes from ifile and write the encoded bit stream
to ofile. We first determine the frequencies, write the header
data with these frequencies so that the receiver can rebuild the
tree for decoding.*/
int encode(const char* ifile, const char *ofile) {
    FILE *fin, *fout;
    if ((fin = fopen(ifile, "rb")) == NULL) {
        perror("Failed to open input file");
        return -1;
    }
    if ((fout = fopen(ofile, "wb")) == NULL) {
        perror("Failed to open output file");
        fclose(fin);
        return -1;
    }

    determine_frequency(fin);
    stack = (int *) calloc(num_active - 1, sizeof(int));
    allocate_tree();

    add_leaves();
    write_header(fout);
    build_tree();
    fseek(fin, 0, SEEK_SET);
    int c;
    while ((c = fgetc(fin)) != EOF)
        encode_alphabet(fout, c);
    flush_buffer(fout);
    free(stack);
    fclose(fin);
    fclose(fout);

    return 0;
}
/*First get the node index assigned to the alphabet. Then,
use the parent_index table to move up the tree, retrieving
the new parent using the index stored in the internal nodes. The
value of the bit to be emitted is simply encoded by whether
the index assigned to the internal node is either odd or even.
Remember that we always combine consecutive nodes, and
hence, left children will always have odd indices and right
children will always have even indices. Thus, if we are left
child, we emit a 1; or a 0, otherwise*/
void encode_alphabet(FILE *fout, int character) {
    int node_index;
    stack_top = 0;
    node_index = leaf_index[character + 1];
    while (node_index < num_nodes) {
        stack[stack_top++] = node_index % 2;
        node_index = parent_index[(node_index + 1) / 2];
    }
    while (--stack_top > -1)
        write_bit(fout, stack[stack_top]);
}



/*To decode Huffman encoded bit stream, we first need to
determine the alphabet frequency. This information is provided
in the header of the input file. We therefore read the header
file, and use the frequencies to build the binary coding tree*/
int decode(const char* ifile, const char *ofile) {
    FILE *fin, *fout;
    if ((fin = fopen(ifile, "rb")) == NULL) {
        perror("Failed to open input file");
        return -1;
    }
    if ((fout = fopen(ofile, "wb")) == NULL) {
        perror("Failed to open output file");
        fclose(fin);
        return -1;
    }

    if (read_header(fin) == 0) {
        build_tree();
        decode_bit_stream(fin, fout);
    }
    fclose(fin);
    fclose(fout);

    return 0;
}
/*To decode the bit-stream, we retrieve one bit at a time and
start at the top of the coding tree, the root. Depending on the
bit value, we decide whether to visit the left subtree or the
right subtree. Remember that the left subtree will always have
an odd index, and the right tree an even index*/
void decode_bit_stream(FILE *fin, FILE *fout) {
    int i = 0, bit, node_index = nodes[num_nodes].index;
    while (1) {
        bit = read_bit(fin);
        if (bit == -1)
            break;
        node_index = nodes[node_index * 2 - bit].index;
        if (node_index < 0) {
            char c = -node_index - 1;
            fwrite(&c, 1, 1, fout);
            if (++i == original_size)
                break;
            node_index = nodes[num_nodes].index;
        }
    }
}

/*The function write_bit writes a bit value bit to file f.
first check if the buffer is full. If it is, we write the buffer to
the file. Otherwise, the bit is packed to the existing buffer*/
int write_bit(FILE *f, int bit) {
    if (bits_in_buffer == MAX_BUFFER_SIZE << 3) {
        size_t bytes_written =
            fwrite(buffer, 1, MAX_BUFFER_SIZE, f);
        if (bytes_written < MAX_BUFFER_SIZE && ferror(f))
            return INVALID_BW;
        bits_in_buffer = 0;
        memset(buffer, 0, MAX_BUFFER_SIZE);
    }
    if (bit)
        buffer[bits_in_buffer >> 3] |=
            (0x1 << (7 - bits_in_buffer % 8));
    ++bits_in_buffer;
    return 0;
}

/*If the bits sent to the buffer stops before the buffer is fully
packed, we must ensure that the bits in the buffer are written to
the file. Function flush_buffer () does precisely that*/
int flush_buffer(FILE *f) {
    if (bits_in_buffer) {
        size_t bytes_written =
            fwrite(buffer, 1,
                (bits_in_buffer + 7) >> 3, f);
        if (bytes_written < MAX_BUFFER_SIZE && ferror(f))
            return -1;
        bits_in_buffer = 0;
    }
    return 0;
}

int read_bit(FILE *f) {
    if (current_bit == bits_in_buffer) {
        if (eof_input)
            return -1;
        else {
            size_t bytes_read =
                fread(buffer, 1, MAX_BUFFER_SIZE, f);
            if (bytes_read < MAX_BUFFER_SIZE) {
                if (feof(f))
                    eof_input = 1;
            }
            bits_in_buffer = bytes_read << 3;
            current_bit = 0;
        }
    }

    if (bits_in_buffer == 0)
        return -1;
    int bit = (buffer[current_bit >> 3] >>
        (7 - current_bit % 8)) & 0x1;
    ++current_bit;
    return bit;
}


/* Since write_header() uses the nodes array, it is important to
write this header after inserting all of the leaves, but before
building the coding tree*/
int write_header(FILE *f) {
     int i, j, byte = 0,
         size = sizeof(unsigned int) + 1 +
              num_active * (1 + sizeof(int));
     unsigned int weight;
     char *buffer = (char *) calloc(size, 1);
     if (buffer == NULL)
         return -1;

     j = sizeof(int);
     while (j--)
         buffer[byte++] =
             (original_size >> (j << 3)) & 0xff;
     buffer[byte++] = (char) num_active;
     for (i = 1; i <= num_active; ++i) {
         weight = nodes[i].weight;
         buffer[byte++] =
             (char) (-nodes[i].index - 1);
         j = sizeof(int);
         while (j--)
             buffer[byte++] =
                 (weight >> (j << 3)) & 0xff;
     }
     fwrite(buffer, 1, size, f);
     free(buffer);
     return 0;
}
/*When decoding the encoded file, we simply read back the
header and retrieve the active alphabets and corresponding
frequencies. Once this is done, we can rebuild the coding tree.*/
int read_header(FILE *f) {
     int i, j, byte = 0, size;
     size_t bytes_read;
     unsigned char buff[4];

     bytes_read = fread(&buff, 1, sizeof(int), f);
     if (bytes_read < 1)
         return -1;
     byte = 0;
     original_size = buff[byte++];
     while (byte < sizeof(int))
         original_size =
             (original_size << (1 << 3)) | buff[byte++];

     bytes_read = fread(&num_active, 1, 1, f);
     if (bytes_read < 1)
         return -1;

     allocate_tree();

     size = num_active * (1 + sizeof(int));
     unsigned int weight;
     char *buffer = (char *) calloc(size, 1);
     if (buffer == NULL)
         return -1;
     fread(buffer, 1, size, f);
     byte = 0;
     for (i = 1; i <= num_active; ++i) {
         nodes[i].index = -(buffer[byte++] + 1);
         j = 0;
         weight = (unsigned char) buffer[byte++];
         while (++j < sizeof(int)) {
             weight = (weight << (1 << 3)) |
                 (unsigned char) buffer[byte++];
         }
         nodes[i].weight = weight;
     }
     num_nodes = (int) num_active;
     free(buffer);
     return 0;
}


/* In case of not entering valid arguments, the help of the program is shown to facilitate the execution */
void print_help() {
      fprintf(stderr,
          "USAGE: ./huffman [encode | decode] "
          "<input out> <output file>\n");
}


/*A single main to use de program*/
int main(int argc, char **argv) {
    if (argc != 4) {
        print_help();
        return 1;
    }
    init();
    if (strcmp(argv[1], "encode") == 0)
        encode(argv[2], argv[3]);
    else if (strcmp(argv[1], "decode") == 0)
        decode(argv[2], argv[3]);
    else
        print_help();
    finalise();
    return 0;
}
