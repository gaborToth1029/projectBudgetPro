 import { configureStore } from "@reduxjs/toolkit";
 import userReducer from 'feature/auth';

 export const store = configureStore({
    reducer: {
      user: userReducer, 
    },
    devTools: process.env.NODE_ENV !== 'production'

});
 