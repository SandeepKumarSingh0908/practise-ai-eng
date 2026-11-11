#Log
## Why I'm doing this (2026-11-07)
- Am moving my carrier to AI engineering, where i want to build, ship real LLM apps, not just read blogs or books and procastinate rather than putting actual effort.
- I will be finishing it on or before 100 days.
- Will be studying 1 hours a day and if get more time will push it extra hours too.

#Week 1
#DAY-0
- Using qwen2.5:7b model pulled from ollam for lab related stuffs
- Currently on 16gb ram mac, Will update if i face any issue later

#Day-1
- Learned about how LLM works at a very high level and produces output.
- Tried prompting same question multiple times and got different types of token everytime explaining or answering the same thing.
- What amazed me is how a totally false question can be answered by a model in pretty confident tone, which confirms there is no fact check at real time, if question is pretty niche, or less likely to be appeared in training data set.

#Day-2
- Learned about tokens
- input tokens are way cheaper than the output ones because of the computation and resource consumption.
- What amazed me is two things -:
  - Firstly how loading a 80 mb pdf and giving 3 relevant page from pdf, can drastically impact the quality of output.
  - Billing is done on the output token, And prompting with code snippets,hindi lang, table or something which is not well covered by the tokenizer vocab, can impact the cost.

#Day-3
- Learned about images, audio support as input by these LLM's, although eventually they get trimmed down token.
- Intresting fact i came across is given these amazing support of images and audios, there comes an extra layer of pre-cautions like it can cost more (so crop and keep only relevant, prefer text over images and trascribe over audio unless you need the tone ad emotion to get captured by LLM, always check does our model is text or vision model too, because beig text model OCR process is involved and if image is not of high quality then data will be corrupted even before it reaches the model.
- Intresting scripts is there in day03 lab. 
