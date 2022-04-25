DROP TABLE IF EXISTS PrintLogs;

CREATE TABLE "PrintLogs"(
    "printid" INTEGER NOT NULL,
    "filename" TEXT NOT NULL,
    "printer" TEXT NOT NULL,
    "datetime" TEXT NOT NULL,
    "copies" INTEGER NOT NULL,
    PRIMARY KEY("printid", AUTOINCREMENT)
);