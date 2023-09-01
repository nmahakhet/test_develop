import { createStore } from "vuex";
import { getInfo, updateInfo, getTp } from "@/api/pipingApi";

export default createStore({
  state: {
    infoDatas: [],
    formInfoData: {},
    testpointData: [],
  },
  getters: {},
  mutations: {
    setInfoDatas(state, data) {
      state.infoDatas = data;
    },
    setFormInfoDatas(state, data) {
      state.formInfoData = data;
    },
    setTestPointData(state, data) {
      state.testpointData = data;
    },
  },
  actions: {
    async fetchInfoData({ commit }) {
      const response = await getInfo();
      commit("setInfoDatas", response);
    },
    setFormInfoDatas({ commit }, data) {
      commit("setFormInfoDatas", data);
    },
    setInfoDatas({ commit }, data) {
      commit("setInfoDatas", ...data);
    },
    async updateInfo({ commit }, params: any) {
      await updateInfo(params.id, params.data);
    },
    setTestPoint({ commit }, datas: any) {
      commit("setTestPointData", datas);
    },
  },
  modules: {},
});
