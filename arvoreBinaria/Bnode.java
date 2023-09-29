

public class Bnode{
    // variáveis de instância - substitua o exemplo abaixo pelo seu próprio
    private int x;
    private Bnode esq, dir;
    
    public Bnode(int v){
        x=v;
        esq = dir = null;
    }
    
    public void add(int v){
        if(v<x){
            if(esq!=null){
                esq.add(v);
            }
            else{
                esq = new Bnode(v);
            }
        }
        else{
            if(dir!=null){
                dir.add(v);
            }
            else{
                dir = new Bnode(v);
            }
        }
    }
    
    public void show(){
        if(dir!=null) dir.show();
        System.out.println(x);
        if(esq!=null) esq.show();
    }
    
    public boolean find(int valor){
        if(valor==x){
            return true;
        }
        else{
            if(valor<x){
                if(esq!=null){
                   return esq.find(valor); 
                }
                else{
                    return false;
                }
            }
            else{
                if(dir!=null){
                    return dir.find(valor);
                }
                else{
                    return false;
                }
            }
        }
    }
    
    public void showLess(int valor){
        if(x<valor){
            System.out.println(x +" | ");
            if(esq!=null){
                esq.showLess(valor);
            }
            if(dir!=null){
                dir.showLess(valor);
            }
        }
        else{
            if(esq!=null){
                esq.showLess(valor);
            }
        }
    }
    
    public int quantidade(){
        if(dir!=null && esq!=null){
            return dir.quantidade()+esq.quantidade();
        }
        //so esquerda
        if(dir==null && esq!=null){
            return esq.quantidade();
        }
        //so direita
        if(dir!=null && esq==null){
            return dir.quantidade();
        }
        else{
            return 1;
        }
    }
    
    public int maior(){
        if(dir!=null){
            return dir.maior();
        }
        else{
            return x;
        }
    }
    
    public int menor(){
        if(esq!=null){
            return esq.menor();
        }
        else{
            return x;
        }
    }
    
    public void mostrarNivel(int valor, int nivel){
        if(nivel<valor){
            esq.mostrarNivel(valor,nivel+1);
            dir.mostrarNivel(valor,nivel+1);
        }
        else{
            System.out.print(x +" | ");
        }
    }
    
    public int somaNaoFolha() {
        int soma = 0;
        
        if (esq != null || dir != null) { // Verifica se o nó não é folha
            soma += x; // Adiciona o valor do nó à soma
            
            if (esq != null) {
                soma += esq.somaNaoFolha(); // Chama recursivamente para a subárvore esquerda
            }
            
            if (dir != null) {
                soma += dir.somaNaoFolha(); // Chama recursivamente para a subárvore direita
            }
        }
        
        return soma;
    }
    
    
    public boolean isEstritamenteBinaria() {
        if (esq == null && dir == null) {
            // O nó não tem filhos, é permitido
            return true;
        } else if (esq != null && dir != null) {
            // O nó tem dois filhos, é permitido. Faz chamada recursiva para continuar execução.
            return esq.isEstritamenteBinaria() && dir.isEstritamenteBinaria();
        } else {
            // O nó tem apenas um filho, o que não é permitido
            return false;
        }
    }
    

    public boolean isDegenerada() {
        if (esq != null && dir == null) {
            // O nó atual tem apenas um filho à esquerda
            
            if (esq.isDegenerada()) { //continua recursivamente até o fim
                return true;
            }


        } else if (esq == null && dir != null) {
            // O nó atual tem apenas um filho à direita
            
            if (dir.isDegenerada()) {
                return true;
            }


        } else if (esq == null && dir == null) {
            // O nó atual é uma folha (é permitido em uma árvore degenerada)
            
            
            return true;
        }
        
        return false; // Condição de árvore degenerada não atendida
    }
    
    public void printFormatoParentesis() {
        System.out.print("(" + x);
        
        //Entra no a esquerda e depois a direta
        //quebra linha após
        if(esq != null){
            esq.printFormatoParentesis();
        };
        if(dir != null){
            dir.printFormatoParentesis();

        };
        System.out.print(")");



    }


    public int alturaArvore(){
        int leftDepth = (esq == null) ? 0 : esq.alturaArvore(); //se nao houverem nós após, o valor é zero. Começa a somar daí pra cima
        int rightDepth = (dir == null) ? 0 : dir.alturaArvore();
        
        return Math.max(leftDepth, rightDepth) + 1;
    }
    

}





