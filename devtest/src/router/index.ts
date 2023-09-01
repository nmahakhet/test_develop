import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import PipingView from "../views/PipingView.vue";
import DetailsView from "../views/DetailsView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "piping",
    component: PipingView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/details/:id",
    name: "DetailsView",
    component: DetailsView,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
