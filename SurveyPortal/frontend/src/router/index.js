import { createWebHistory, createRouter } from "vue-router";
import HelloWorld from "@/components/HelloWorld";
import Screen from "@/components/Screen";
import Eligibility from "@/components/eligibility"

const routes = [
  {
    path: "/",
    name: "HelloWorld",
    component: HelloWorld,
  },
  {
    path: "/screen/:email/:zipcode",
    name: "Screen",
    component: Screen,
    props: true
  },
  {
    path: "/eligibility/:eligible/:zipcode",
    name: "Eligibility",
    component: Eligibility,
    props: true
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
