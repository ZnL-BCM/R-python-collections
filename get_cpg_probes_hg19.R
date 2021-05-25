# R/4.0.5
# Creates a csv file for lifting over Illumina CpG probes to genomic coordinates
# Under the hg19 coordinates


if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install("IlluminaHumanMethylation450kanno.ilmn12.hg19")
# Load library
library(IlluminaHumanMethylation450kanno.ilmn12.hg19)
# Disable scientific notation
options(scipen=100)


data("IlluminaHumanMethylation450kanno.ilmn12.hg19")
Data = getAnnotation(IlluminaHumanMethylation450kanno.ilmn12.hg19)

ChrArr <- Data@listData$chr
PosArr <- Data@listData$pos
NameArr <- Data@rownames
StrandArr <- Data@listData$strand

DF = data.frame(
  ChrArr, PosArr-1, PosArr, NameArr, 
  ".", StrandArr
  )
colnames(DF) <- c("chr", "start", "end", "probe", "skip", "strand")

DF <- DF[order(DF$chr, DF$start), ]

# Write to BED or csv
write.table(DF, "Illumina_cpg_probes_hg19.bed", row.names=FALSE, col.names=FALSE, 
            quote=FALSE, sep="\t")
write.csv(DF, "Illumina_cpg_probes_hg19.csv", row.names=FALSE)
