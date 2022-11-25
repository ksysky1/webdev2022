//캡스톤2 입력박스씬- output1 코드
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Output1Drag : MonoBehaviour
{
    public GameObject Box1;
    public GameObject Box2;
    public GameObject Box3;
    public GameObject Box0;
    private float Dist0 = 0;
    private float Dist1 = 0;
    private float Dist2 = 0;
    private float Dist3 = 0;
    private float ShortDist = 0;
    private int flag = -1;// 다른 데 들어간적 없음

    // Start is called before the first frame update
    void Start()
    {
        Dist0 = Vector3.Distance(Box0.transform.position, transform.position);
        Dist1 = Vector3.Distance(Box1.transform.position, transform.position);
        Dist2 = Vector3.Distance(Box2.transform.position, transform.position);
        Dist3 = Vector3.Distance(Box3.transform.position, transform.position);

        if(Dist2 >= Dist1){
            if(Dist3 >= Dist1){
                ShortDist = Dist1;
                if(Dist1 >= Dist0)
                    ShortDist = Dist0;
            }
            else
                ShortDist = Dist3;
        }
        else{
            if(Dist3 >= Dist2)
                ShortDist = Dist2;
            else
                ShortDist = Dist3;
        }
    }

    // Update is called once per frame
    void Update()
    {
       if(flag == -1){
            if(ShortDist == Dist0){
                Vector3 destination = Box0.transform.position + new Vector3(12,30,10); //box0내의 정해진 위치로 이동하게 하기.
                transform.position = Vector3.MoveTowards(transform.position, destination, 1);
            }
            else if(ShortDist == Dist1){
                Vector3 destination = Box1.transform.position + new Vector3(-25,30,-30); //box1내의 정해진 위치로 이동하게 하기.
                transform.position = Vector3.MoveTowards(transform.position, destination, 1);
            }
            else if(ShortDist == Dist2){
                Vector3 destination = Box2.transform.position + new Vector3(-25,30,-30); //box2내의 정해진 위치로 이동하게 하기.
                transform.position = Vector3.MoveTowards(transform.position, destination, 1);
            }
            else if(ShortDist == Dist3){
                Vector3 destination = Box3.transform.position + new Vector3(-25,30,-30); //box3내의 정해진 위치로 이동하게 하기.
                transform.position = Vector3.MoveTowards(transform.position, destination, 1);
            }
       }


        if(transform.position == Box1.transform.position + new Vector3(-25,30,-30)){
            flag = 0; // 입력 박스 안에 들어간 적 있음 표시
        }

        else if(transform.position == Box2.transform.position + new Vector3(-25, 30, -30)){
            flag = 1; // 처리 박스 안에 들어간 적 있음 표시
        }


        if(flag == 0 || flag == 1){// 답이 틀렸을 때(출력 글자가 입력박스나 처리박스로 들어갔을 때)
            Vector3 ReturnDest = Box0.transform.position + new Vector3(12, 30, 10); //박스0내의 정해진 위치로 보내기
            transform.position = Vector3.MoveTowards(transform.position, ReturnDest, 2);
        }

    }
}
