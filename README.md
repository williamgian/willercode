# willercode


db <- "X:/NYCAPS/Long Beach/Charter Provisionals v2.0.accdb"

con <- odbcConnectAccess2007(db)

sqlTables(con, tableType = "TABLE")$TABLE_NAME

prov <- sqlFetch(con, "Charter Provisionals Detail")


odbcClose(con)


prov <- subset(prov, prov$`Rule Number` == "5.4.2B")

prov <- merge(x=prov[,c("SSN", "Employee #", "Applicant Name", "Agency Code", "Title Code", "Title Description", "Rule Number", "CS Status")], y=agy[,c("agypayrollcode", "agyshortdescription")], by.x='Agency Code', by.y='agypayrollcode', all.x=T)

write.csv(prov, file = "C:/Users/wgian/Documents/prov_expired_20160608.csv", row.names = F)
