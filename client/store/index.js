export const LOGIN_MUTATION = Symbol();

export const state = () => ({
   user: {username: '', email: '', id: 0, password: ''},
   isAuth: false,
});

export const mutations = {
  [LOGIN_MUTATION](state, user){
    Object.assign(state.user, user);
    state.isAuth = true;

    localStorage.setItem('auth', JSON.stringify(user));
  }
};
