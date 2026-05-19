#!/bin/bash
jupyter nbextension disable --sys-prefix nbgrader/main || true
jupyter nbextension disable --sys-prefix nbgrader/assignment_list/main || true
jupyter serverextension disable --sys-prefix nbgrader.server_extensions.assignment_list || true
