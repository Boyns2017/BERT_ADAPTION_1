; Auto-generated. Do not edit!


(cl:in-package table_simulator-msg)


;//! \htmlinclude Robot.msg.html

(cl:defclass <Robot> (roslisp-msg-protocol:ros-message)
  ((informedHuman
    :reader informedHuman
    :initarg :informedHuman
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Robot (<Robot>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Robot>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Robot)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name table_simulator-msg:<Robot> is deprecated: use table_simulator-msg:Robot instead.")))

(cl:ensure-generic-function 'informedHuman-val :lambda-list '(m))
(cl:defmethod informedHuman-val ((m <Robot>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:informedHuman-val is deprecated.  Use table_simulator-msg:informedHuman instead.")
  (informedHuman m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Robot>) ostream)
  "Serializes a message object of type '<Robot>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'informedHuman)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Robot>) istream)
  "Deserializes a message object of type '<Robot>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'informedHuman)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Robot>)))
  "Returns string type for a message object of type '<Robot>"
  "table_simulator/Robot")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Robot)))
  "Returns string type for a message object of type 'Robot"
  "table_simulator/Robot")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Robot>)))
  "Returns md5sum for a message object of type '<Robot>"
  "1b1fa61214ab58b35a5b3de4cf13a2d4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Robot)))
  "Returns md5sum for a message object of type 'Robot"
  "1b1fa61214ab58b35a5b3de4cf13a2d4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Robot>)))
  "Returns full string definition for message of type '<Robot>"
  (cl:format cl:nil "uint8 informedHuman~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Robot)))
  "Returns full string definition for message of type 'Robot"
  (cl:format cl:nil "uint8 informedHuman~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Robot>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Robot>))
  "Converts a ROS message object to a list"
  (cl:list 'Robot
    (cl:cons ':informedHuman (informedHuman msg))
))
