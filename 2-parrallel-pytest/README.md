
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

if  --dist=loadscope is kept in the ini file, and adding these lines to the conftest 

```
def pytest_collection_modifyitems(items):
    """Automatically group non-parallel_safe tests onto a single worker."""
    for item in items:
        if not item.get_closest_marker("parallel_safe"):
            item.add_marker(pytest.mark.xdist_group("serial"))

```

it will make it so you only have to tag a test that is parrallel_safe in order to run it