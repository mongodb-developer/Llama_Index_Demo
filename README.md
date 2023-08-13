# LlamaIndex Example

![llama](https://www.aktagon.com/images/articles/LlamaIndex.png)


LlamaIndex examples can be found in the examples folder of the LlamaIndex repository. To get started, you can download the examples folder by cloning the repository:

```
$ git clone https://github.com/jerryjliu/llama_index.git

Navigate to the repository and verify its contents:
```

Then cd llama_index
```
$ ls
LICENSE                data_requirements.txt  tests/
MANIFEST.in            examples/              pyproject.toml
Makefile               experimental/          requirements.txt
README.md              llama_index/             setup.py
```

# Next, navigate to the following folder:

```
$ cd examples/paul_graham_essay
```
This directory contains LlamaIndex examples based on Paul Graham's essay, "What I Worked On". Comprehensive examples are provided in TestEssay.ipynb, but for this tutorial, we'll focus on a simple example to get LlamaIndex up and running.

# Build and Query Index
Create a new .py file with the following content:
```
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)
#This code builds an index over the documents in the data folder (which contains the essay text). Then, run the following code:
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)

```
This should yield a response similar to: "The author wrote short stories and tried to program on an IBM 1401."
Viewing Queries and Events Using Logging
In a Jupyter notebook, you can view info and/or debugging logging using the following code snippet:

```
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
You can set the logging level to DEBUG for more verbose output, or use level=logging.INFO for less detailed information.
```
Saving and Loading
By default, data is stored in-memory. To persist data to disk (under ./storage):
```
index.storage_context.persist()
To reload data from disk:
from llama_index import StorageContext, load_index_from_storage
```
Rebuild the storage context

```
storage_context = StorageContext.from_defaults(persist_dir="./storage")
```
Load the index

```
index = load_index_from_storage(storage_context)
```
Please note that some of the paths and specific details might need to be adapted based on your environment and the structure of your project.

[llamaindex](https://www.llamaindex.ai/)

[Github](https://github.com/jerryjliu/llama_index)
