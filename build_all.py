import os
import pdoc
import shutil
from distutils.core import setup

from Cython.Build import cythonize


release_dir = 'release'
docs_dir = 'docs'
skip_dirs = ['examples', 'tests']
to_compile_dir = r'cx_pyfolio'
to_compile_files = []
skip_files = ['__init__.py']

os.makedirs(release_dir, exist_ok=True)

file_to_compil = []
for subdir, dirs, files in os.walk(to_compile_dir):

    skip = False
    for i in skip_dirs:
        if i in subdir:
            skip = True
            break

    if skip:
        for file in files:
            filepath = os.path.join(subdir, file)

            dst = os.path.join(release_dir, subdir)
            os.makedirs(dst, exist_ok=True)

            dst = os.path.join(release_dir, filepath)
            shutil.copy(filepath, dst)

    else:
        for file in files:
            filepath = os.path.join(subdir, file)

            if file.endswith('.py') and file not in skip_files:
                file_to_compil.append(filepath)

            else:
                dst = os.path.join(release_dir, subdir)
                os.makedirs(dst, exist_ok=True)

                dst = os.path.join(release_dir, filepath)
                shutil.copy(filepath, dst)


setup(
    ext_modules=cythonize(
        file_to_compil,
        language_level=3,
        build_dir="build",
        compiler_directives={
            'always_allow_keywords': True,
            'embedsignature': True,
            'language_level': 3
        },
    )
)

output_dir = os.path.join(os.getcwd(), docs_dir)
os.makedirs(output_dir, exist_ok=True)

modules = [to_compile_dir]  # Public submodules are auto-imported
context = pdoc.Context()

modules = [pdoc.Module(mod, context=context)
           for mod in modules]
pdoc.link_inheritance(context)


def recursive_htmls(mod):
    yield mod.name, mod.html(show_source_code=False)
    for submod in mod.submodules():

        skip = False
        for i in skip_dirs:
            if i in submod.name:
                skip = True
                break

        if skip:
            continue

        yield from recursive_htmls(submod)


for mod in modules:
    for module_name, html in recursive_htmls(mod):
        with open(os.path.join(output_dir, f"{module_name}.html"), "w", encoding='utf-8') as f:
            f.write(html)


dst = os.path.join(release_dir, docs_dir)
shutil.rmtree(dst, ignore_errors=True)
shutil.copytree(docs_dir, dst)
