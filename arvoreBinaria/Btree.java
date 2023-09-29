
public class Btree{
    private Bnode raiz;
    
    public Btree(){
        raiz = null;
    }
    
    public void add(int v){
        if(raiz!=null){
            raiz.add(v);
        }
        else{
            raiz = new Bnode(v);
        }
    }
    
    public void show(){
        if(raiz!=null) raiz.show();
    }
    
    public boolean find(int valor){
        if(raiz!=null) return raiz.find(valor);
        else return false;
    }
    
    public void showLess(int valor){
        if(raiz!=null) raiz.showLess(valor);
    }
    
    public int quantidade(){
        if(raiz!=null) return raiz.quantidade();
        else return 0;
    }
    
    public int maior(){
        if(raiz!=null) return raiz.maior();
        else return -999;
    }
    
    public int menor(){
        if(raiz!=null) return raiz.menor();
        else return -999;
    }
    
    public void mostrarNivel(int valor){
        if(raiz!=null)raiz.mostrarNivel(valor,1);
    }
    
    public int somaNaoFolha() {
        if (raiz != null) {
            return raiz.somaNaoFolha();
        }
        return 0; // Retorna 0 se a árvore estiver vazia.
    }
    
    
    public boolean isEstritamenteBinaria() {
        if (raiz != null) {
            return raiz.isEstritamenteBinaria();
        }
        return true; // Uma árvore vazia é estritamente binária
    }

    public boolean isDegenerada() {
        if (raiz != null) {
            return raiz.isDegenerada();
        }
        return true; // Uma árvore vazia é considerada degenerada
    }

    public void printFormatoParentesis() {
        if (raiz != null) {
            raiz.printFormatoParentesis();
        }
    }
    

    public int alturaArvore(){
        return (raiz == null) ? 0 : raiz.alturaArvore(); //verificação se a raiz é nula
    }

}
