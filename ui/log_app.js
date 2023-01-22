const routes=[
    {path:'/logowanie-klient',component:client_log},
    {path:'/logowanie-pracownik',component:employee_log}
]

const router=new VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
})

const app = Vue.createApp({})

app.use(router)
app.mount('#log_app')