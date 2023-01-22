const books_list_client={template:`

<table class="table table-stripped">
<thead>
    <tr>
        <th>
            Tytuł
        </th>
        <th>
            Autor
        </th>
        <th>
            Cena
        </th>
    </tr>
</thead>
<tbody>
    <tr v-for="b in books">
        <td>{{b.TytulKs}}</td>
        <td>{{b.AutorKs}}</td>
        <td>{{b.CenaKs}}</td>
    </tr>
</tbody>
</table>
    </div>

</div>
</div>
</div>
`,

data(){
    return{
        books:[],
        zmiana:false,
        modalTitle:"",
        ISBN:"",
        TytulKs:"",
        AutorKs:"",
        CenaKs:0,
        DodalIdP:0
    }
},
methods:{
    refreshData(){
        axios.get(variables.API_URL+"ksiazka")
        .then((response)=>{
            this.books=response.data;
        });
    },
    addClick(){
        this.zmiana=false,
        this.modalTitle="Dodaj książkę";
        this.ISBN="";
        this.TytulKs="";
        this.AutorKs="";
        this.CenaKs=0;
        this.DodalIdP=0;
    },
    editClick(b){
        this.zmiana=true;
        this.modalTitle="Edytuj książkę";
        this.ISBN=b.ISBN;
        this.TytulKs=b.TytulKs;
        this.AutorKs=b.AutorKs;
        this.CenaKs=b.CenaKs;
        this.DodalIdP=b.DodalIdP;
    },
    createClick(){
        axios.post(variables.API_URL+"ksiazka",{
            ISBN:this.ISBN,
            TytulKs:this.TytulKs,
            AutorKs:this.AutorKs,
            CenaKs:this.CenaKs,
            DodalIdP:this.DodalIdP   
        })
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });
    },
    updateClick(){
        axios.put(variables.API_URL+"ksiazka",{
            ISBN:this.ISBN,
            TytulKs:this.TytulKs,
            AutorKs:this.AutorKs,
            CenaKs:this.CenaKs,
            DodalIdP:this.DodalIdP
        })
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });
    },
    deleteClick(id){
        if(!confirm("Potwierdź usunięcie")){
            return;
        }
        axios.delete(variables.API_URL+"ksiazka/"+id)
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });
    }
},
mounted:function(){
    this.refreshData();
}

}