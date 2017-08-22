#!/bin/sh

START_ID=$1
END_ID=$2
TABLE_NAME=YOUR_BIG_TABLE_NAME
OUT=$TABLE_NAME\_$MIN_ID\_$MAX_ID.csv # column separte by "|"

#######################
sqlplus -s "USER_NAME/PASSWD@ORACLE_DB" << END_SQL > /dev/null
set colsep "|"
set heading on
set timing off
set echo off
set term off
set timeout off
set linesize 49999
set trimspool on
set pagesize 0
set trim on
set wrap off
set feedback off
set newpage 0
set arraysize 5000
SPOOL $OUT
select * from $TABLE_NAME where id between $START_ID and $END_ID;
spool off
exit

END_SQL
#######################

########################################################################################
## Don't use 'select *'. You'd better trim each column and format datetime field in your query.
## Then concatenate all together. 
########################################################################################
