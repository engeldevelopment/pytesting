test:
	@pytest

report:
	@pytest --junit-xml=report.xml
