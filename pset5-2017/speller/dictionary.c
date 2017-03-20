/**
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// declare node* of root which is the beginning of our dictionary trie
node* root = NULL;
int num_words;

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    /* declare a crawler called cursor that will move through the dictionary trie and point it
     * at the dictionary root
     */
    node *cursor = root;
    
    int i = 0;
    
    // while we haven't yet reached the end of the word
    while (word[i] != '\0')
    {
        int letter = word[i];
        // convert input word to lowercase and normalize to index (tolower(c) - 'a')
        if (letter == '\'')
        {
            letter = 26;
        }
        else
        {
            letter = tolower(word[i]) - 'a';
        }

        if (!cursor->children[letter])
        {
            // word is misspelled
            return false;
        }
        else
        {
            // move to next letter in input word and next node in trie
            i++;
            cursor = cursor->children[letter];
        }
    }
    // once at end of input word, confirm if is_word is true
    if (!cursor->is_word)
    {
        return false;
    }
    else
    {
        return true;
    }
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{
    // try to open dictionary
    FILE *fp = fopen(dictionary, "r");
    if (fp == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        unload();
        return false;
    }
    
    // malloc some space for the first, or root, node
    root = calloc(1, sizeof(node));
    // declare the cursor pointer, which will crawl through the trie.
    node *cursor = NULL;
    
    num_words = 0;
    
    // while we haven't yet reached the end of the file
    while (!feof(fp))
    {        
        // point the crawler to the root
        cursor = root;
        
        //fseek(fp, -1, SEEK_CUR);
        
        // iterate through each line
        for (int c = fgetc(fp); c != '\n' && c != EOF; c = fgetc(fp))
        {
            /* index the character of the word that we're looking at to a number [0,26]
             * set apostrophe to 26
             */
            if (c == '\'')
            {
                c = 26;
            }
            else
            {
                c = tolower(c) - 'a';
            }
            // if value of children[i] is NULL
            if (!cursor->children[c])
            {
                // malloc a new node of proper size and check that it was successful
                cursor->children[c] = calloc(1, sizeof(node));
                if (!cursor->children[c])
                {
                    printf("Out of heap memory!\n");
                    return 1;
                }
                // have children[i] point to it
                cursor = cursor->children[c];   
            }
            else
            {
                // move to new node and continue iterating
                cursor = cursor->children[c];
            }
        }
        // after reaching the end of a word, set is_word to true and increment num_words
        cursor->is_word = true;
        
        if (!feof(fp))
        {
            num_words++;
        }
    }
    
    fclose(fp);
    return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    // TODO
    return num_words;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    if (free_trie_node(root))
    {
        return true;
    }
    
    return false;
}

bool free_trie_node(struct node *node)
{
    if (!node)
    {
        return true;
    }
    
    // iterate over all children in each node
    for (int c = 0; c < 27; c++)
    {
        // if a child is not null then free it again
        if (node->children[c] != NULL)
        {
            free_trie_node(node->children[c]);
        }
    }
    free(node);
    
    return true;
}
