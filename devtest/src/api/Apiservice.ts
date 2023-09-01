/* eslint-disable no-useless-catch */
// src/api/ApiService.ts
import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from "axios";
import { Config } from "@/config";

class ApiService {
  private axiosInstance: AxiosInstance;

  constructor() {
    const { baseURL } = Config;
    this.axiosInstance = axios.create({
      baseURL,
    });
  }

  public async request<T>(
    config: AxiosRequestConfig
  ): Promise<AxiosResponse<T>> {
    try {
      const response = await this.axiosInstance.request<T>(config);
      return response;
    } catch (error) {
      throw error;
    }
  }
}

export default new ApiService();
