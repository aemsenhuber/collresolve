import setuptools

module = setuptools.Extension(
	"collresolve",
	sources = [ "collresolve.c", "collresolve_python.c",
			"cambioni2019/accretion_efficiency.c", "cambioni2019/orbital_hnr.c", "cambioni2019/collision_classifier.c" ]
)

setuptools.setup(
    name = "collresolve",
    version = "1.3",
    author = "Alexandre Emsenhuber",
    author_email = "emsenhuber@lpl.arizona.edu",
    description = "Analyse and predict outcomes of collision in N-body",
    long_description = open( "README.md", "r" ).read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/aemsenhuber/collresolve",
    ext_modules = [ module ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
    ],
)
