clean:
	rm -rf dist package neonbranch.zip

dist: lambda
	poetry build

package: dist
	poetry run pip install --upgrade --target package dist/*.whl

neonbranch.zip: package
	cd package; zip -r ../neonbranch.zip . -x '*.pyc'
