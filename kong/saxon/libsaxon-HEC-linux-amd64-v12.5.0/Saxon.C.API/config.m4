PHP_ARG_ENABLE(saxon,
    [Whether to enable the "saxon" extension],
    [  --enable-saxon      Enable "saxon" extension support])

if test $PHP_SAXON != "no"; then
    CXXFLAGS="-std=c++14"
    PHP_REQUIRE_CXX()
    PHP_ADD_INCLUDE(graalvm)
    PHP_SUBST(SAXON_SHARED_LIBADD)
    PHP_ADD_LIBRARY(stdc++, 1, SAXON_SHARED_LIBADD)
    PHP_ADD_LIBRARY(dl, 1, SAXON_SHARED_LIBADD)
    PHP_ADD_LIBRARY(saxon-hec-12.5.0, 1, SAXON_SHARED_LIBADD)
    PHP_NEW_EXTENSION(saxon, php8_saxon.cpp SaxonProcessor.cpp DocumentBuilder.cpp XQueryProcessor.cpp  XsltExecutable.cpp Xslt30Processor.cpp XPathProcessor.cpp SchemaValidator.cpp XdmValue.cpp XdmItem.cpp XdmNode.cpp XdmAtomicValue.cpp XdmFunctionItem.cpp XdmMap.cpp XdmArray.cpp SaxonApiException.cpp SaxonCGlue.c SaxonCProcessor.c  SaxonCXPath.c, $ext_shared)
fi

