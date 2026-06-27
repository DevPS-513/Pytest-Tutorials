
## A simple example of running pytest in parallel using xdist

Example where a normal pytest command takes 5 seconds to run, but running in parallel takes only 2.7 seconds. Overall steps are when in the root dir could be something along the lines of:

```
deactivate
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
```

after which -n and other such arguments are available to pytest , also --dist=loadscope   # keeps same module/class on same worker (more stable)


```
python -m  pytest -n 4 ./validation/scenarios.py -k food
plugins: xdist-3.8.0, bdd-8.1.0
4 workers [4 items]     
....                                                                        [100%]
================================ 4 passed in 2.71s ================================
(.venv) @AcerNitro2:~/39-Parrallel-Pytest/2-parrallel-pytest$ 

```


```
python -m  pytest ./validation/scenarios.py -k food


================================ 4 passed in 5.04s ================================
(.venv) @AcerNitro2:~/39-Parrallel-Pytest/2-parrallel-pytest$ 

```

Here are common options for running pytest in parallel using the `xdist` plugin.

**Worker count:**
```bash
-n auto        # auto-detect based on CPU cores
-n 4           # fixed 4 workers
-n logical     # use logical CPUs (includes hyperthreading)
```

**Distribution modes (`--dist`):**
```bash
--dist=load        # default — sends tests to first available worker (fastest)
--dist=loadscope   # keeps same module/class on same worker (more stable)
--dist=loadfile    # keeps same file on same worker
--dist=no          # disables distribution (serial), even with -n set
```

**Output:**
```bash
-s             # show print() output from tests
-v             # verbose — show each test name
-v --tb=short  # shorter tracebacks on failure
```

**Filtering (works same as without xdist):**
```bash
-m parallel_safe          # only marked tests
-m "not parallel_safe"    # exclude marked tests
-k food                   # keyword match
```

**Failure control:**
```bash
-x             # stop on first failure
--max-fail=2   # stop after 2 failures
```

**Combining them:**
```bash
python -m pytest -n auto --dist=loadscope -v -m parallel_safe ./validation/scenarios.py
```

**Most useful for your setup right now:**
```bash
python -m pytest -n auto --dist=loadfile -v -s ./validation/scenarios.py
```

`--dist=loadfile` is the safest choice since your BDD scenarios are split across feature files.