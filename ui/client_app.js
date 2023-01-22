const routes=[
    {path:'/oferta',component:books_list_client}
]

const router=new VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
})

const app = Vue.createApp({})

app.use(router)
app.mount('#client_app')