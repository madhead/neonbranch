clean:
	rm -rf lambda/dist lambda/package lambda/neonbranch.zip

lambda/dist: lambda
	cd lambda && poetry build

lambda/package: lambda/dist
	cd lambda && poetry run pip install --upgrade --target package dist/*.whl

lambda/neonbranch.zip: lambda/package
	cd lambda/package; zip -r ../neonbranch.zip . -x '*.pyc'
