# Missioni-GPT
[image here]



## Overview
- Implements a proof-of-concenpt for querying personal PDF documents using LangChain, Pinecone and ChatGPT.
- Documents embeddings code is omitted [available soon]
- Streamlint UI from Streamlit-chatGPT[https://github.com/joeychrys/streamlit-chatGPT]

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
cd streamlit-chatGPT
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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
