// hash_util.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_HASH_OUTPUT 64

// djb2 hash function (returns -1 as not yet implemented)
int djb2_hash(const char *input, char *out, size_t out_len){ 
    (void)input; 
    (void)out; 
    (void)out_len; 
    return -1; 
}
// FNV-1a hash function (returns -1 as not yet implemented)
int fnv1a_hash(const char *input, char *out, size_t out_len){ 
    (void)input; 
    (void)out; 
    (void)out_len; 
    return -1; 
}
// Salted hash function combining raw hash with salt (returns -1 as not yet implemented)
int salt_hash(const char *raw_hash, const char *salt, char *out, size_t out_len){ 
    (void)raw_hash; 
    (void)salt; 
    (void)out; 
    (void)out_len; 
    return -1; 
}

// Main function to verify the skeleton compiles successfully
int main()
    { printf("hash_util.c skeleton compiled OK\n");
    
    return 0;
    }