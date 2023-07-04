#######################
drop user dummy;
drop user jaylen;
drop user ReadOnly;
drop user Developer;
#######################

CREATE ROLE IF NOT EXISTS 'ReadOnly';
CREATE ROLE IF NOT EXISTS 'Developer';

CREATE USER IF NOT EXISTS dummy IDENTIFIED BY 'dummy';
CREATE USER IF NOT EXISTS jaylen IDENTIFIED BY 'jaylen';

GRANT SELECT ON demo.* to ReadOnly;
GRANT SELECT, INSERT, UPDATE, DELETE ON demo.* to Developer;

GRANT ReadOnly TO dummy;
GRANT ReadOnly TO jaylen;

SET DEFAULT ROLE ALL TO dummy;
SET DEFAULT ROLE ALL TO jaylen;

FLUSH PRIVILEGES;