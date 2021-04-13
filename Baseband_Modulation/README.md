# Baseband Modulation in a Noisy Environment
 ------------------------------------------
### University of Costa Rica
#### September, 2020
 ------------------------------------------

## Integrants
1. Brown Ramírez, Timna Belinda  B61254
2. Esquivel Molina, Brandon B52571
3. Sosa, Heillen B26567
4. Bermúdez, Daniel B50999
5. Hernández, Miguel A42600


## MATLAB
A baseband digital modulator, a Gaussian additive white noise channel and a baseband digital demodulator are 

# Description 
An encoder is simulated for an information source consisting of an uncompressed text, audio or image file, to obtain a sequence of bits of information (at the source encoder output) bf (ℓ), then an encoder is simulated of channel programmed on this sequence of information bits bf (ℓ) to obtain the sequence of transmitted bits (at the output of the channel encoder) bc (ℓ).

In this stage, a programmed baseband digital modulator is simulated that uses a PAM modulation scheme of order M, on this sequence of coded bits bc (ℓ) to obtain a sequence of samples x (k), which represents the modulated signal x (t). and finally a programmed baseband digital demodulator is simulated that uses a PAM modulation scheme of order M, to recover the bits of a sequence of information b ∗ c (ℓ), from a sequence of received samples x ∗ (k ), which represents the received modulated signal x ∗ (t).

# How to run
Download or clone de rep, go into the src folder and run the main.m file

# Paths
Maybe you will need to copy and paste de functions .m into your MATLAB default path to run without Errors.
