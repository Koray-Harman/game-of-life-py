@ECHO OFF

REM Command file for test execution

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  test      	to execute nosetests
	echo.  placeholder	to make HTML files named index.html in directories
	goto end
)

if "%1" == "test" (
	nosetests tests
	if errorlevel 1 exit /b 1
	echo.
	goto end
)

if "%1" == "placeholder" (
	%SPHINXBUILD% -b dirhtml %ALLSPHINXOPTS% %BUILDDIR%/dirhtml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/dirhtml.
	goto end
)

:end