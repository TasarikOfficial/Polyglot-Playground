package main
import ("fmt"; "net/http"; "os"; "time")
func main() {
 if len(os.Args)<2 { fmt.Println("usage: go run url_checker.go <url>"); return }
 client:=http.Client{Timeout:5*time.Second}
 start:=time.Now(); res,err:=client.Get(os.Args[1])
 if err!=nil { fmt.Println("offline:",err); return }
 defer res.Body.Close()
 fmt.Printf("%s · %d · %s\n",res.Status,time.Since(start).Milliseconds(),os.Args[1])
}
