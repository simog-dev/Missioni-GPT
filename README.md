# Missioni-GPT
![Application image](https://github.com/simog-dev/Missioni-GPT/blob/main/docs/app_img.jpeg?raw=true)

## Overview
- Implements a proof-of-concept for querying personal PDF documents using LangChain, Pinecone and ChatGPT to answer question about Unipi mission request.
- Documents embeddings code is omitted [available soon]
- Streamlint UI from [Streamlit-chatGPT](https://github.com/joeychrys/streamlit-chatGPT)

## Installation

1. Clone the repository

```bash
git clone https://github.com/joeychrys/streamlit-chatGPT.git
```

2. Modify the `.env` file inside the `src` directory and add your `OPENAI_API_KEY`. To obtain access to Pinecone vectors, contact the repository owner.

```bash
OPENAI_API_KEY=yourapikey
PINECONE_API_KEY=contact repo owner
```

3. Create and activate a new virtual environment

```bash
python -m venv env
source env/bin/activate
```
4. Move to project directory

```bash
cd Missioni-GPT
```

5. Install the required packages

```bash
pip install -r requirements.txt
```

6. Run the Streamlit application

```bash
streamlit run src/main.py
```

## Usage

Once the application is running, you can interact with it by following the on-screen instructions at `http://localhost:8501`

## TODO

- Adjust form and content of the PDF from which the answers are extracted. At the moment, the document is composed of the set of PDFs that expose the different procedures for the missions without any adjustments. For getting better answers, it would be optimal to clean the PDFs of unnecessary text and the transformation of tables to text.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
