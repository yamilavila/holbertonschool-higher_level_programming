GENERAL OBJECTIVES:

    Why Python programming is awesome
You know why.

    What’s an interactive test
Searches for pieces of text that look like interative Python sessions and then executes those sessions to verify that they work exactly as shown, this is call doctest.

    Why tests are important
* To check that a module's docstring are up-to-date by verifying that all interactive examples still work as documented.

* To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.

* To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of "literate testing" or "executable documentation".

    How to write Docstrings to create tests
First, what is a docstring? Well, is a string to document a Python module, class, function or method, so programmers can understand what it does without having to read the details of implementation.
	The simplest way to start using doctest is to end each module M with:
		if __name__ == "__main__":
		    import doctest
		    doctest.testmod()
	doctest then exaamines docstring in module M.

	Runnig the module as a script causes the examples in the docstring to get executed and verified: 
		python M.py

This won't display anything unless theres any failure. In case of failure, it will print the failure in the stdout and the final line of output is ***Test Failed*** N failures., where N is the number of examples that failed.

Run it with the -v switch instead:
		python M.py -v
and a detailed report of all examples tried is printed to standard output, along with assorted summaries at the end.


    How to write documentation for each module and function

For the testfile() function it can be done with:

		import doctest
		doctest.testfile("example.txt")

This short script executes and verifies any interactive Python examples contained in the file example.txt. The file content is treated as if it were a single giant docstring; the file doesn't need to contain Python program. ***For examples visit https://docs.python.org/3.9/library/doctest.html***


    What are the basic option flags to create tests

To be continue...

    How to find edge cases

