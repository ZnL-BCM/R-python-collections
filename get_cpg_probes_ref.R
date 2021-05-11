# R/4.0.5
# Creates a csv file for lifting over Illumina CpG probes to genomic coordinates


library(IlluminaHumanMethylation450kanno.ilmn12.hg19)


data("IlluminaHumanMethylation450kanno.ilmn12.hg19")
Data = getAnnotation(IlluminaHumanMethylation450kanno.ilmn12.hg19)


DF = data.frame(
  Data@listData$chr, Data@listData$pos-1, Data@listData$pos, Data@rownames, 
  ".", Data@listData$strand
  )
colnames(DF) <- c("chr", "start", "end", "probe", "skip", "strand")

DF <- DF[order(DF$chr, DF$start), ]

# Write to BED or csv
write.table(DF, "Illumina_cpg_probes_hg19.bed", row.names=FALSE, col.names=FALSE, 
            quote=FALSE, sep="\t")
write.csv(DF, "Illumina_cpg_probes_hg19.csv", row.names=FALSE)
