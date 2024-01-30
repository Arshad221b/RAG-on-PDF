# Smart PDF Reader

![smart pdf reader](/screenshots/IMG_4161.JPG)

## Overview

The Smart PDF Reader is a comprehensive project that harnesses the power of the Retrieval-Augmented Generation (RAG) model over a Large Language Model (LLM) powered by Langchain. Additionally, it utilizes the Pinecone vector database to efficiently store and retrieve vectors associated with PDF documents. This approach enables the extraction of essential information from PDF files without the need for training the model on question-answering datasets.

## Features

1. **RAG Model Integration**: The project seamlessly integrates the Retrieval-Augmented Generation (RAG) model, combining a retriever and a generator for effective question answering.

2. **Langchain-powered Large Language Model (LLM)**: Langchain enhances the capabilities of the Large Language Model, providing advanced language understanding and context.

3. **Pinecone Vector Database**: Utilizing Pinecone's vector database allows for efficient storage and retrieval of document vectors, optimizing the overall performance of the Smart PDF Reader.

4. **PDF Information Extraction**: The system focuses on extracting information directly from PDF files, eliminating the need for extensive training on question answering datasets.

5. **User-Friendly Interface**: The project includes a user-friendly interface for interacting with the PDF reader, making it accessible to users with various levels of technical expertise.

## Dependencies

- Python 3.x
- PyTorch
- Transformers library
- Langchain
- Pinecone

You can install the required dependencies using the following command:

```bash
pip install torch transformers langchain pinecone
```


## License

This project is licensed under the [MIT License](LICENSE).

---

## Blog
Read about [Vector Database Architecture](https://arshad-kazi.com/vector-database-and-its-architecture/)
