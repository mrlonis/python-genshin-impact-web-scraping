################################################################################
# Configuration file for markdownlint.
#
# https://github.com/markdownlint/markdownlint/blob/master/docs/configuration.md
#
# Order of preference for markdownlint config file (first one wins):
#   ${PWD}/.mdlrc
#   ${HOME}/.mdlrc
################################################################################

all
exclude_rule 'MD013'
rule 'MD007', :indent => 2