# Connectify

Connectify is a web application designed to facilitate seamless interaction with AI platforms, particularly focusing on text-based AI models like ChatGPT and others. It addresses the challenge of working with AI models that have specific prompt length limitations, making it difficult to process large text inputs efficiently.

## Problem Statement

Many AI models, including ChatGPT and similar platforms, have restrictions on the maximum length of text prompts they can handle effectively. This limitation poses challenges when dealing with tasks such as summarization or querying large documents, where the input text exceeds the prompt length.

Additionally, copying and pasting large text excerpts manually for processing.

## Solution Overview

Connectify offers a solution to these challenges by providing a user-friendly web interface for interacting with AI models. The key features of Connectify include:

1. **PDF Reading**: Users can upload PDF documents directly to Connectify, eliminating the need to manually copy and paste text from external sources.

2. **AI Integration**: Connectify integrates with various AI platforms, leveraging their capabilities for tasks such as summarization, question answering, and text generation.

3. **Prompt Management**: Connectify automatically manages prompt length limitations by breaking down large text inputs into smaller, manageable chunks. This ensures optimal utilization of AI models without compromising on performance.

4. **Output Presentation**: The application presents AI-generated outputs in a conversational format, mimicking the style of interaction with a chatbot. This enhances user experience and makes the results more accessible.

## Technology Stack

Connectify utilizes the following technologies to deliver its functionality:

- **OpenAI API**: Integrates with OpenAI's powerful AI models for natural language processing tasks.
- **FAISS Vector Store**: Utilizes FAISS for efficient similarity search and retrieval of text embeddings.
- **OpenAI Embeddings**: Leverages pre-trained embeddings for text representation and similarity computation.
- **RecursiveCharacterTextSplitter**: A text processing tool used for splitting large documents into manageable segments.

## Usage

To use Connectify, follow these steps:

1. Visit the Connectify website.
2. Upload the PDF document you want to analyze or summarize.
3. Enter your query or prompt in the provided input field.
4. Click on the "Submit" or "Generate" button to initiate processing.
5. Review the AI-generated response presented on the screen.
6. Optionally, refine your query or interact further with the system.

