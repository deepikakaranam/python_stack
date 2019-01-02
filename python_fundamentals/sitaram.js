function Linkedlist(){
    var length=0;
    var head=null;
    var node=function(element){
        this.element=element;
        this.next=null;
    };
    this.size=function(){
        return length;
    };
    this.head=function(){
        return head;
    };
    this.add=function(element){
        var node=new node(element);
        if(head===null){
            head=node;
        }else{
           var currentnode=head;
           while(currentnode.next){
               currentnode.next=node;
           }
           length++
        }
    };
    return currentnode;
}

Linkedlist(5);