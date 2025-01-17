<h3 align="center">🎄</h3>
<h3 align="center">aoc</h3>
<h6 align="center">Advent of Code</h6>

<p align="center">
<img src="https://github.com/wysockipiotr/aoc/workflows/Tests/badge.svg?branch=main" />
<a href="https://codecov.io/gh/wysockipiotr/aoc">
  <img src="https://codecov.io/gh/wysockipiotr/aoc/branch/main/graph/badge.svg?token=LB9U2LORRO"/>
</a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

###### Quickstart
1. Use Python **^3.8**
<pre>
<code>
<b>$ pyenv local</b> 3.8.6
</code>
</pre>

2. Make sure [Poetry](https://python-poetry.org/) is installed for the selected Python interpreter

3. Run the code for the daily puzzle
<pre>
<code>
<b>$ poetry run</b> aoc solve --day DAY_NUMBER
</code>
</pre>

###### Generating daily solution code
<pre>
<code>
<b>$ poetry run</b> aoc create --day NEXT_DAY_NUMBER --name TASK_NAME
</code>
</pre>

###### Running tests
<pre>
<code>
<b>$ poetry run</b> pytest
</code>
</pre>

###### Formatting
<pre>
<code>
<b>$ poetry run</b> black .
<b>$ poetry run</b> isort .
</code>
</pre>
