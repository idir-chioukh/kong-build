from saxoncee import PySaxonProcessor
from pathlib import Path
import secrets
import psutil
import gc
import sys
data_path = (Path(__file__) / '../../data').resolve()

count = 0
prev = (mi := psutil.Process().memory_info)().rss

iterations = sys.argv[1]

for _ in range(int(iterations)):
    processor = PySaxonProcessor(license=True)
    builder = processor.new_document_builder()
    xslt = processor.new_xslt30_processor()
    long_lived_transform = xslt.compile_stylesheet(stylesheet_file=str((data_path / "books.xsl")))
    long_lived_doc = builder.parse_xml(xml_file_name=(str(data_path / "books.xml")))

    sv = processor.make_string_value
    austen = sv("Jane Austen")

    for n in range(int(iterations) * 10):
        xslt = processor.new_xslt30_processor()
        transform = xslt.compile_stylesheet(stylesheet_file=str((data_path / "books.xsl")))
        transform.set_parameter("top-author", austen)
        transform.set_parameter("title", sv(secrets.token_hex(16)))
        long_lived_transform.set_parameter("top-author", austen)
        long_lived_transform.set_parameter("title", sv(secrets.token_hex(16)))
        doc = builder.parse_xml(xml_file_name=(str(data_path / "books.xml")))

        transform.set_global_context_item(xdm_item=doc)
        result = transform.apply_templates_returning_value(xdm_node=doc)
        transform.set_global_context_item(xdm_item=long_lived_doc)
        result = transform.apply_templates_returning_value(xdm_node=long_lived_doc)
        long_lived_transform.set_global_context_item(xdm_item=doc)
        result = long_lived_transform.apply_templates_returning_value(xdm_node=doc)
        long_lived_transform.set_global_context_item(xdm_item=long_lived_doc)
        result = long_lived_transform.apply_templates_returning_value(xdm_node=long_lived_doc)
        if n % 100 == 0:
            m = mi().rss
            print(f"{m:,} ({m - prev:,})")
            prev = m
        print(".", end="")

    print("+")
    gc.collect()

m = mi().rss
print(f"{m:,} ({m - prev:,})")
prev = m
