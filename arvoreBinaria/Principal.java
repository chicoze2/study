public class Principal{
    public static void main(String args[]){
        Btree a = new Btree();
        
        a.add(50);
        a.add(30);
        a.add(70);
        a.add(40);
        a.add(10);
        a.add(80);
        a.add(60);

        a.add(90);
        
        // Exercicio 1: Encontrar valor na lista
        // System.out.println(a.find(10));
        
        // Exercicio 2: Encontrar valor menor que parametro:
        // a.showLess(40);

        //Exercicio 3: Retornar soma dos nós na folha
        // System.out.println(a.quantidade());

        //Exercicio 4: Retornar maior valor armazenado
        // System.out.println(a.maior());

        //Exercicio 5: Retornar menor valor armazenado
        // System.out.println(a.menor());

        //Exercicio 6: Printar nós que estão em um determinado nivel
        // a.mostrarNivel(2);
        
        //Exercicio 7: Soma dos nós não-folha ( aqueles que possuem filhos )
        // System.out.println(a.somaNaoFolha());

        //Exercicio 8: Verificar se a árvore é estritamente binária (0 ou 2 filhos)
        //remover uma entrada para testar
        // System.out.println(a.isEstritamenteBinaria());

        //Exercicio 9: Verificar se a árvore é degenerada, isto é; possui um nó por nivel
        // a.add(1);
        // a.add(2);
        // a.add(3);
        // a.add(4);

        // System.out.println(a.isDegenerada());

        //Exercicio 10: Imprimir arvore formatada em parênteses. 
        //Remover 3 valores ajuda
        // a.printFormatoParentesis(); 


        //Exercicio 11: Encontrar maior caminho na arvore.
        // System.out.println(a.alturaArvore());


        //Exercicio 12: Escrever os metodos para encontrar a altura de uma arvore binaria.
        System.out.println(a.alturaArvore());

        
        //Exercicio 13: Construir metodo bool para retornar:  V - Arvore possui pelo menos uma repetição de elemento
        //                                                    F - A arvore nao possui repetições
    }
}
