
generate-requirements:
  #!/bin/bash
  pip-compile --output-file=- --resolver=backtracking > requirements.txt
