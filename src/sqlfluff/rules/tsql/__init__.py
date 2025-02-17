"""The tsql rules plugin bundle.

This plugin bundles linting rules which apply exclusively to TSQL. At some
point in the future it might be useful to spin this off into a separate
installable python package, but so long as the number of rules remain
low, it makes sense to keep it bundled with SQLFluff core.
"""

from sqlfluff.core.plugin import hookimpl


@hookimpl
def get_rules():
    """Get plugin rules.

    NOTE: Rules are imported only on fetch to manage import times
    when rules aren't used.
    """
    from sqlfluff.rules.tsql.TQ01 import Rule_TQ01

    return [Rule_TQ01]
