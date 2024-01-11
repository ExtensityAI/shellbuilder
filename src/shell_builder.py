import argparse
import json
import os
import sys
from pathlib import Path
from symai import Expression


class PackageInitializer(Expression):
    def forward(self, package_name: str, description: str, shell_style: str = '', **kwargs):
        super().__init__(**kwargs)
        self.package_dir = Path.home() / '.symai/packages/'

        if not os.path.exists(self.package_dir):
            os.makedirs(self.package_dir)

        os.chdir(self.package_dir)

        vals = package_name.split('/')
        try:
            username = vals[0]
            package_name = vals[1]
        except:
            print('Invalid package name: {git_username}/{package_name}')
            exit(1)

        package_path = os.path.join(self.package_dir, username, package_name)
        if os.path.exists(package_path):
            print('Package already exists')
            exit(1)

        print('Creating package...')
        os.makedirs(package_path)
        os.makedirs(os.path.join(package_path, 'src'))

        with open(os.path.join(package_path, '.gitignore'), 'w'): pass
        with open(os.path.join(package_path, 'LICENSE'), 'w') as f:
            f.write('MIT License')
        with open(os.path.join(package_path, 'README.md'), 'w') as f:
            f.write('# ' + package_name + f"\n## {description}\n" + f"""
## Install SymbolicAI

```bash
pip install symbolicai
```

See more info at the original [Repository](https://github.com/ExtensityAI/symbolicai).

### Installation

```bash
$> sympkg i {username}/{package_name}
```

### Usage

```bash
$> symsh --style={username}/{package_name}
```

""")
        with open(os.path.join(package_path, 'requirements.txt'), 'w'): pass
        with open(os.path.join(package_path, 'package.json'), 'w') as f:
            json.dump({
                'version': '0.0.1',
                'name': username+'/'+package_name,
                'description': description,
                'expressions': [
                    {'module': 'src/styles', 'type': 'StyledFunction'},
                    {'module': 'src/styles', 'type': 'StyledConversation'},
                    {'module': 'src/styles', 'type': 'RetrievalAugmentedStyledConversation'}
                ],
                'run': {'module': 'src/styles', 'type': 'StyledConversation'},
                'dependencies': []
            }, f, indent=4)
        with open(os.path.join(package_path, 'src', 'styles.py'), 'w') as f:
            f.write('''from symai.extended import Conversation, RetrievalAugmentedConversation
from symai import Function


SHELL_CONTEXT = """{template}"""


class StyledFunction(Function):
    @property
    def static_context(self) -> str:
        return SHELL_CONTEXT


class StyledConversation(Conversation):
    @property
    def static_context(self) -> str:
        return SHELL_CONTEXT


class RetrievalAugmentedStyledConversation(RetrievalAugmentedConversation):
    @property
    def static_context(self) -> str:
        return SHELL_CONTEXT + """[Description]
This program is a retrieval augmented indexing program. It allows to index a directory or a git repository and retrieve files from it.
The program uses a document retriever to index the files and a document reader to retrieve the files.
The document retriever uses neural embeddings to vectorize the documents and a cosine similarity to retrieve the most similar documents.

[Program Instructions]
If the user requests functions or instructions, you will process the user queries based on the results of the retrieval augmented memory."""'''.format(template=shell_style))
            return '\nPackage created successfully at: ' + package_path

