class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        def gene_mutation(gene1, gene2):
            diff_count = 0
            for c1, c2 in zip(gene1, gene2):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 1:
                        break
            
            return diff_count == 1

        gene_set = set(bank)

        if endGene not in gene_set:
            return -1

        gene_set.add(startGene)
        gene_set.add(endGene)

        gene_dict = collections.defaultdict(set)

        for gene1 in gene_set:
            for gene2 in gene_set:
                if gene_mutation(gene1, gene2):
                    gene_dict[gene1].add(gene2)
                    gene_dict[gene2].add(gene1)

        visit = set()
        queue = [(0, startGene)]

        while queue:
            count, gene = queue.pop(0)
            visit.add(gene)
            
            if gene == endGene:
                return count
            
            count += 1
            for next_gene in gene_dict[gene]:
                if next_gene not in visit:
                    queue.append((count, next_gene))
        
        return -1
            