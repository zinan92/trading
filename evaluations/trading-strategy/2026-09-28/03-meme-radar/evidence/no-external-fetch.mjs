import fs from 'node:fs';
const writeLog=entry=>{
  const file=process.env.MEME_RADAR_TRIAL_NETWORK_LOG;
  if(!file)return;
  fs.appendFileSync(file,JSON.stringify({...entry,blocked:true})+'\n',{mode:0o600});
};
const nativeFetch=globalThis.fetch;
globalThis.fetch=async(input,init)=>{
  const raw=typeof input==='string'?input:input?.url;
  const u=new URL(raw);
  if(['127.0.0.1','localhost','::1'].includes(u.hostname))return nativeFetch(input,init);
  writeLog({method:init?.method||'GET',host:u.hostname,path:u.pathname});
  throw new Error('Product Lab trial blocks external provider calls');
};
