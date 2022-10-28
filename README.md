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

It was clarified users input is given batched; not streamed. What does this mean? *Receive all user input into a variable, and locate all phrases which begin with the input.

