# Simple example of browser-use

To run the project, navigate to the project folder and create a virtual enviornment using uv or any other method.

```bash
uv venv --python 3.11
```

Then, activate it:

#### For Windows:

```bash
.venv\Scripts\activate
```

#### For macOS/Linux:

```bash
source .venv/bin/activate
```

Once activated, install the dependecies:

```bash
uv pip install browser-use
```

```bash
playwright install
```

## Add OpenAI key

create a .env file in the project directory and add your OpenAI API key.

```bash
OPENAI_API_KEY=your-openai-api-key
```

## Create screenshots folder

create a `screenshots` folder in the main project directory. You can skip this step if you don't want to save screenshots recording.

```bash
mkdir screenshots
```

Now you are ready to run `agent.py` script. To change the website it visits and the task it performs, simply change the `task` argument in the Agent instance.