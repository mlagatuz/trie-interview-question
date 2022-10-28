# trie-interview-question

## Motivation

During a coding round, I was asked a question about the data structure "Trie". As the interviewer was explaining the question on the whiteboard, I recognized the ds which could be used would be a "Trie". While I struggled with the answer during the interview, I knew I needed to attempt and complete the problem on my own. It's a work in progress, while I continue to study, code, and practice.

## Question

Given a list of phrases, and a user input, return all phrases which begin with user input 

```
list_of_phrases = [ "this is a description", this is why we speak", \
                    "some sort of phrase", "that is what I said", \
                    "those are my pictures" ] 
```

Let's provide some input and resulting outputs

```
user input: "tho"

result = [ "those are my pictures" ]
```

```
user input: "this"

result = [ "this is a description", "this is why we speak", \
           "that is what I said", "those are my pictures" ]
```

```
user input: "th"
result = [ "this is a description", "this is why we speak", \
           "that is what I said", "those are my pictures" ] 
```

It was clarified users input is given batched; not streamed. What does this mean? *Receive all user input into a variable, and locate all phrases which begin with the input.*

## Workflow

Since I don't have the interviewer in front of me, let's make my own assumptions (for the sake of simplicity)

One way of solving this would be to search the first word of every phrase against our input string. This would be a O(n) time complexity, for every search we initiate. If we search for "th", this would be a O(n) search through the entire list_of_phrases.

Let's take the idea of "trie" data structure. I'll assume we can take the first word of every phrase, store it in the trie, and it would look similar to this (given our assumption and our list_of_phrases):

```

                        [root]------+
                           |        |  
                          [t]      [s]
                           |        |
                +----+----[h]      [o]
                |    |     |        |
               [o]  [a]   [i]      [m]
                |    |     |        |
               [s]  [t]   [s]      [e]
                |    |     |        |
               [e]  [*]   [*]      [*]
                |
               [*]
```

Okay, given an input, such as "th", we will have a path of: *[root] --> [t] --> [h]*. At every node along the path, let's store the indices of all valid list_of_phrases at that point. 

```
input: "th"
list_of_phrases = [ "this is a description", this is why we speak", \
                    "some sort of phrase", "that is what I said", \
                    "those are my pictures" ]

traverse trie: [root]
valid_phrase_set: [none]

traverse trie: [t]
valid_phrase_indices: [0,1,3,4]

traverse trie: [h]
valid_phrase_indices: [0,1,3,4]
```

At every step along the path, you're going to have a list of indices! What if the input is "tho"

```
input: "tho"
list_of_phrases = [ "this is a description", this is why we speak", \
                    "some sort of phrase", "that is what I said", \
                    "those are my pictures" ]

traverse trie: [root]
valid_phrase_set: [none]

traverse trie: [t]
valid_phrase_indices: [0,1,3,4]

traverse trie: [h]
valid_phrase_indices: [0,1,3,4]

traverse trie: [o]
valid_phrase_indices: [4]
```

When I take a step back, I notice something interesting: as you're closer to [root], the set of indices is larger. As you're farther from [root], you're set becomes smaller. In other words, the searching list_of_phrases becomes smaller as your move farther from [root]. This makes sense, as your searching and creating subsets as your traverse this trie.

